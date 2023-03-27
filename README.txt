機能：

Pi NetwokのブロックチェーンエクスプローラのAPIを利用して以下を行います。

（１）疑わしいアドレスに１０００π以上の転送をリストアップ
（２）アドレス毎に送金量を累積加算する
（３）（１）でリストアップしたアドレスで（１）（２）を実行(*)

(*)１度確認したアドレスでの再実行しない


Function:

Utilizing the API of the Pi Network blockchain explorer, the following will be performed:

(1) List up transfers of 1000π or more to suspicious addresses.
(2) Accumulate the transfer amount for each address.
(3) Execute (1) and (2) for the addresses listed in (1).(*)

(*) Do not execute again on addresses that have already been checked.



Usage:

python piTracePayments.py {address} [-to] [-from]

{address} : root address for tracing
[-to]   : tracing only sent address
[-from] : tracing only recieved address

example:
python piTracePayments.py GDS73TBQ5L2KX2D7EWMY43O4NB3RZXE4XFTH6SBRZK3QZJCB2L63GQHU 

python piTracePayments.py GDS73TBQ5L2KX2D7EWMY43O4NB3RZXE4XFTH6SBRZK3QZJCB2L63GQHU -to
