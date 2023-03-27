
#### pip install requests

import json
import requests
import sys
import re

LIM=200
AMTH=1000
d_adr_send={}
d_adr_recv={}
l_adr_checked=[]



args = sys.argv
root_adr    = str(args[1])

#print("==============================")
#print(type(args))

f_mode = 0

for xxx in args:
  if xxx=="-to":
    f_mode = 1
  if xxx=="-from":
    f_mode = 2






def adr2dict( addr , cursor , limit ):
  #ll=[]
  #print(addr)
  url = "https://api.mainnet.minepi.com/accounts/" + addr + "/payments?cursor=" +  str(cursor) + "&limit=" + str(limit) +"&order=asc"
  session = requests.Session()
  dd = session.get(url)
  jd = json.loads(dd.text)
  return jd



def listPayments( d_json ):
  id="unkown"
  errmsg="d_json in listPayments is NOT expected"
  if not ( '_embedded' in d_json.keys() ):
    print( errmsg )
  else:
    if not ( 'records' in d_json['_embedded'].keys() ):
      print( errmsg )
    else:
      l_adr = d_json['_embedded']['records']
      for dd in l_adr:
        errmsg="Dict 'dd' in listPayments is unexpected data. "
        if not ( 'type' in dd.keys()):
          print(errmsg)
        else:
          if (dd['type']=="payment"):
            amount = dd['amount']
            if ( float(amount) > AMTH -1 ):
              buf = ""
              buf = buf + 'amount'
              buf = buf + ','
              buf = buf + dd['amount']
              buf = buf + ','
              buf = buf + 'form'
              buf = buf + ','
              buf = buf + dd['from']
              buf = buf + ','
              buf = buf + 'to'
              buf = buf + ','
              buf = buf + dd['to']
              buf = buf + ','
              buf = buf + 'created_at'
              buf = buf + ','
              buf = buf + dd['created_at']
              buf = buf + ','
              print(buf)


#d_adr_send={}
#d_adr_recv={}
              #####

              if f_mode != 1:
                if not ( dd['from'] in d_adr_send.keys()):
                  d_adr_send[dd['from']]=float(dd['amount'])
                else:
                  d_adr_send[dd['from']]=d_adr_send[dd['from']]+float(dd['amount'])

              if f_mode != 2:
                if not ( dd['to'] in d_adr_recv.keys()):
                  d_adr_recv[dd['to']]=float(dd['amount'])
                else:
                  d_adr_recv[dd['to']]=d_adr_recv[dd['to']]+float(dd['amount'])





      id =  l_adr[ -1 ]['id']
  return id




def roopListPayments ( d_json , adress ):
  while True:
    errmsg="d_json in listPayments is NOT expected"
    if not ( '_embedded' in d_json.keys() ):
      print( errmsg )
      break
    else:
      if not ( 'records' in d_json['_embedded'].keys() ):
        print( errmsg )
        break
      else:
        l_adr = d_json['_embedded']['records']
        if(len(l_adr)==0):
          break
        else:
          next_cs = listPayments(d_json)
          d_json=adr2dict( adress , next_cs , LIM)


def pList ( adr ):
  if  adr not in l_adr_checked:
    djson=adr2dict( adr , "" , LIM)
    roopListPayments( djson , adr )


######### main ##########

pList ( root_adr )
l_adr_checked.append(root_adr)


for k in list(d_adr_send.keys()):
  if k not in l_adr_checked:
    pList ( k )
    l_adr_checked.append(k)

for k in list(d_adr_recv.keys()):
  if k not in l_adr_checked:
    pList ( k )
    l_adr_checked.append(k)


### monitor d_adr_send, d_adr_recv ####

print("#### from adress ####")
d_adr_send_s = sorted(d_adr_send.items(),key=lambda x:x[1], reverse=True)
i=0
for key, value in d_adr_send_s:
  i+=1
  print(i, key, value, sep=',')

print("#### to adress ####")
d_adr_recv_s=sorted(d_adr_recv.items(),key=lambda x:x[1], reverse=True)
i=0
for key, value in d_adr_recv_s:
  i+=1
  print(i, key, value, sep=',')




print("#### balances ####")
l_merge_addr=[]
for k in d_adr_send:
  l_merge_addr.append(k)
for k in d_adr_recv:
  l_merge_addr.append(k)

l_merge_addr = list(set(l_merge_addr))

d_mrg_bl={}
i=0
for k in l_merge_addr:
  i+=1
  url="https://api.mainnet.minepi.com/accounts/" + k 
  session = requests.Session()
  dd = session.get(url)
  jd = json.loads(dd.text)
  balance = jd['balances'][0]['balance']
  d_mrg_bl[k]=float(balance)
  #print(type(d_mrg_bl[k]))

d_mrg_bl_s=sorted(d_mrg_bl.items(),key=lambda x:x[1], reverse=True)
i=0
for key, value in d_mrg_bl_s:
  i+=1
  print(i, key, value, sep=',')


