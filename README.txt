�@�\�F

Pi Netwok�̃u���b�N�`�F�[���G�N�X�v���[����API�𗘗p���Ĉȉ����s���܂��B

�i�P�j�^�킵���A�h���X�ɂP�O�O�O�Έȏ�̓]�������X�g�A�b�v
�i�Q�j�A�h���X���ɑ����ʂ�ݐω��Z����
�i�R�j�i�P�j�Ń��X�g�A�b�v�����A�h���X�Łi�P�j�i�Q�j�����s(*)

(*)�P�x�m�F�����A�h���X�ł̍Ď��s���Ȃ�


Function:

Utilizing the API of the Pi Network blockchain explorer, the following will be performed:

(1) List up transfers of 1000�� or more to suspicious addresses.
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
