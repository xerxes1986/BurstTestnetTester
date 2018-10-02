import time
import requests
import json
import random
import pickle
import logging
# defining the api-endpoint  
#BASE_WALLET_PATH = "http://localhost:8125/burst"
BASE_WALLET_PATH = "https://wallet.dev.burst-test.net/burst"
FEE_NQT = 735000
ONE_BURST = 100000000

def suggest_fee():
    '''
    Gets account details.
    :param account_id: Numeric ID for the account (required)
    :type account_id: str
    :returns: An instance of :class:`Account`
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'suggestFee'})
    return json.loads(response.text)

def get_account(account_id=None):
    '''
    Gets account details.
    :param account_id: Numeric ID for the account (required)
    :type account_id: str
    :returns: An instance of :class:`Account`
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccount',
                                       'account': account_id})
    return json.loads(response.text)

def get_account_ATs(account_id=None):
    '''
    Gets account ATs.
    :param account_id: Numeric ID for the account (required)
    :type account_id: str
    :returns: An instance of :class:`AccountATs`
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountATs',
                                       'account': account_id})
    return json.loads(response.text)

def get_account_block_ids(account_id=None, timestamp=None, first_index=None, last_index=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountBlockIds',
                                       'account': account_id,
                                       'timestamp': timestamp,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index})
    return json.loads(response.text)

def get_account_blocks(account_id=None, timestamp=None, first_index=None, last_index=None, include_transactions=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountBlockIds',
                                       'account': account_id,
                                       'timestamp': timestamp,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index,
                                       'includeTransactions': include_transactions})
    return AccountBlocks.from_json(response.text)

def get_account_current_ask_order_ids(account_id=None, asset=None, first_index=None, last_index=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountCurrentAskOrderIds',
                                       'account': account_id,
                                       'asset': asset,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index})
    return json.loads(response.text)

def get_account_current_ask_orders(account_id=None, asset=None, first_index=None, last_index=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountCurrentAskOrders',
                                       'account': account_id,
                                       'asset': asset,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index})
    return json.loads(response.text)

def get_account_current_bid_order_ids(account_id=None, asset=None, first_index=None, last_index=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountCurrentBidOrderIds',
                                       'account': account_id,
                                       'asset': asset,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index})
    return json.loads(response.text)

def get_account_current_bid_orders(account_id=None, asset=None, first_index=None, last_index=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountCurrentBidOrders',
                                       'account': account_id,
                                       'asset': asset,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index})
    return json.loads(response.text)

def get_account_escrow_transactions(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountEscrowTransactions',
                                       'account': account_id})
    return json.loads(response.text)

def get_account_id(secret_pass=None, public_key=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountId',
                                       'secretPhrase': secret_pass,
                                       'publicKey': public_key})
    return json.loads(response.text)

def get_account_lessors(account_id=None, height=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountLessors',
                                       'account': account_id,
                                       'height': height})
    return json.loads(response.text)

def get_account_public_key(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountPublicKey',
                                       'account': account_id})
    return json.loads(response.text)

def get_account_subscriptions(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountSubscriptions',
                                       'account': account_id})
    return json.loads(response.text)

def get_account_transaction_ids(account_id=None, timestamp=None, _type=None, 
                                subtype=None, first_index=None, last_index=None, 
                                number_of_confirmations=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountTransactionIds',
                                       'account': account_id,
                                       'timestamp': timestamp,
                                       'type': _type,
                                       'subtype': subtype,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index,
                                       'numberOfConfirmations': number_of_confirmations})
    return json.loads(response.text)

def get_account_transactions(account_id=None, timestamp=None, _type=None, 
                                subtype=None, first_index=None, last_index=None, 
                                number_of_confirmations=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountTransactions',
                                       'account': account_id,
                                       'timestamp': timestamp,
                                       'type': _type,
                                       'subtype': subtype,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index,
                                       'numberOfConfirmations': number_of_confirmations})
    return json.loads(response.text)

def get_accounts_with_reward_recipient(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAccountsWithRewardRecipient',
                                       'account': account_id})
    return json.loads(response.text)

def get_assets_by_issuer(account_id=None, first_index=None, last_index=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getAssetsByIssuer',
                                       'account': account_id,
                                       'firstIndex': first_index,
                                       'lastIndex': last_index})
    return json.loads(response.text)

def get_balance(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getBalance',
                                       'account': account_id})
    return json.loads(response.text)
    
def get_escrow_transactions(escrow=None):
    '''
    '''
    #TODO Find and Test
    pass

def get_guaranteed_balance(account_id=None, number_of_confirmations=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getGuaranteedBalance',
                                       'account': account_id,
                                       'numberOfConfirmations': number_of_confirmations})
    return json.loads(response.text)

def get_reward_recipient(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getRewardRecipient',
                                       'account': account_id})
    return json.loads(response.text)

def get_subscription(subscription=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getSubscription',
                                       'subscription': subscription})
    return json.loads(response.text)

def get_subscriptions_to_account(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getSubscriptionsToAccount',
                                       'account': account_id})
    return json.loads(response.text)

def get_unconfirmed_transaction_ids(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getUnconfirmedTransactionIds',
                                       'account': account_id})
    return json.loads(response.text)

def get_unconfirmed_transactions(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'getUnconfirmedTransactions',
                                       'account': account_id})
    return json.loads(response.text)

def rs_convert(account_id=None):
    '''
    '''
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'rsConvert',
                                       'account': account_id})
    return json.loads(response.text)

def send_money(recipient=None, amountNQT=None, secretPhrase=None, feeNQT=None, deadline=None, publicKey=None):
    '''
    '''
    if recipient is None:
        return false
    if amountNQT is None or amountNQT <= 0:
        return false
    if feeNQT is None:
        feesuggestion = suggest_fee()
        feeNQT = feesuggestion['standard']
    if deadline is None:
        deadline=1440
    if publicKey is None:
        response = requests.post(url=BASE_WALLET_PATH, 
                                   data={'requestType': 'sendMoney',
                                           'recipient': recipient,
                                           'amountNQT': amountNQT,
                                           'secretPhrase': secretPhrase,
                                           'feeNQT': feeNQT,
                                           'deadline': deadline})
    else:
        response = requests.post(url=BASE_WALLET_PATH, 
                                   data={'requestType': 'sendMoney',
                                           'recipient': recipient,
                                           'amountNQT': amountNQT,
                                           'secretPhrase': secretPhrase,
                                           'publicKey': publicKey,
                                           'feeNQT': feeNQT,
                                           'deadline': deadline})

    try:
        jsonresponse = json.loads(response.text)
    except:
        jsonresponse = response
    return jsonresponse

def send_money_multi(recipients=None, amountsNQT=None, secretPhrase=None, feeNQT=None, deadline=None):
    '''
    '''
    if recipients is None:
        return False
    if amountsNQT is None:
        return False
    if len(recipients) < 2 or len(recipients) != len(amountsNQT):
        return false
    recipientString = ''
    for i in range(0,len(recipients)):
        if int(amountsNQT[i]) <= FEE_NQT:
            return false
        recipientString = recipientString + str(int(recipients[i])) + ':' + str(int(amountsNQT[i])) + ';'
    recipientString = recipientString[:-1]
    if feeNQT is None:
        feesuggestion = suggest_fee()
        feeNQT = feesuggestion['standard']
    if deadline is None:
        deadline=1440
    response = requests.post(url=BASE_WALLET_PATH,
                             data={'requestType': 'sendMoneyMulti',
                                   'recipients': recipientString,
                                   'secretPhrase': secretPhrase,
                                   'feeNQT': feeNQT,
                                   'deadline': deadline})
    try:
        jsonresponse = json.loads(response.text)
    except:
        jsonresponse = response
    return jsonresponse

def send_money_multi_same(recipients=None, amountNQT=None, secretPhrase=None, feeNQT=None, deadline=None):
    '''
    '''
    if recipients is None:
        return False
    recipientString = ''
    for i in range(0,len(recipients)):
        recipientString = recipientString + str(int(recipients[i])) + ';'
    recipientString = recipientString[:-1]
    if amountNQT is None or amountNQT <= 0:
        return false
    if feeNQT is None:
        feesuggestion = suggest_fee()
        feeNQT = feesuggestion['standard']
    if deadline is None:
        deadline=1440
    response = requests.post(url=BASE_WALLET_PATH, 
                               data={'requestType': 'sendMoneyMultiSame',
                                       'recipients': recipientString,
                                       'secretPhrase': secretPhrase,
                                       'feeNQT': feeNQT,
                                       'deadline': deadline,
                                       'amountNQT': amountNQT})
    try:
        jsonresponse = json.loads(response.text)
    except:
        jsonresponse = response
    return jsonresponse

def set_account_info(name=None, description=None, secretPhrase=None, feeNQT=None, deadline=None):
    '''
    '''
    if feeNQT is None:
        feesuggestion = suggest_fee()
        feeNQT = feesuggestion['standard']
    if deadline is None:
        deadline=1440  
    response = requests.post(url=BASE_WALLET_PATH,
                             data={'requestType': 'setAccountInfo',
                                       'name': name,
                                       'description': description,
                                       'secretPhrase': secretPhrase,
                                       'feeNQT': feeNQT,
                                       'deadline': deadline})
    return json.loads(response.text)


def set_reward_recipient(req=None):
    ''' '''
    response = requests.post(url=BASE_WALLET_PATH, params=req)
    return json.loads(response.text)

def get_free_burst(account=None):
    if account is None:
        return
    return send_money(account,100,'I will take only 500 Burst',2)



print('Generating Accounts')
with open('accts_testnet.pkl','rb') as f:  # Python 3: open(..., 'rb')
    accts = pickle.load(f)
##accts = []
##num = 4096
##acctStr = ''
##for i in range(1,num+1):
##    acct = get_account_id('test'+str(i))
##    accts.append(acct)
##    print('Account#'+str(i)+': '+str(acct['accountRS']))
##    acctStr = acctStr + str(acct['account'])
##    if i % 128 == 0:
##        print('AccountsString: '+acctStr)
##        acctStr = ''
##    else:
##        acctStr = acctStr + ';'
##with open('accts_testnet.pkl','wb') as f:  # Python 3: open(..., 'rb')
##    accts = pickle.dump(accts,f)
###print(acctString)

counter = 0
totalfee = 0 
groupTotal = 10
maxnumberReceivers = 0
feeUnit = 1
while True:
    if counter % 100 == 0:
        feesuggestion = suggest_fee()
        feeNQT = feesuggestion['standard']
        feeUnit = int(feeNQT / FEE_NQT)
    print('loop '+str(counter))
    print('max receivers: '+str(maxnumberReceivers))
    counter = counter + 1
    sender = random.randint(1,4096)
    senderacct = accts[sender-1]
    try:
        balanceresponse = get_balance(senderacct['accountRS'])
        balance = int(balanceresponse['guaranteedBalanceNQT'])
    except:
        logging.exception('error')
        continue
    if balance < 50:
        print('Burst low, getting some new ones:')
        print get_free_burst(senderacct['accountRS'])
        continue
    diceRoll = random.randint(1,100)
    if  diceRoll < 20:
        try:
            print('regular')
            receiver = random.randint(1,4096)
            while sender == receiver:
                receiver = random.randint(1,4096)
            recacct = accts[receiver-1]
            amountToSend = random.randint(FEE_NQT,int(0.2*balance))
            amountInBurst = str(amountToSend / ONE_BURST)
            print(str(sender)+' sends '+amountInBurst+' Burst to '+str(receiver))
            sendreceipt = send_money(recacct['accountRS'],
                                     amountToSend,'test'+str(sender),
                                     random.randint(1,feeUnit)*FEE_NQT,None,recacct['publicKey'])
            tx = sendreceipt['transactionJSON']
            print('Broadcasted: '+str(sendreceipt['broadcasted']))
            fee = int(tx['feeNQT'])/ONE_BURST
            totalfee = totalfee + fee
            print('Fee (Burst): '+str(fee))
            print('Fee Sum (Burst): '+str(totalfee))
            groupTotal = groupTotal + 1
        except:
            logging.exception('error')
            print(sendreceipt)
    elif diceRoll < 80:
        print('multi_out')
        try:
            balanceresponse = get_balance(senderacct['accountRS'])
            balance = int(balanceresponse['guaranteedBalanceNQT'])
            receivers = []
            amounts = []
            totalToSend = 0
            numReceivers=random.randint(12,64)
            for i in range(0,numReceivers):
                prec = random.randint(1,4096)
                while ((prec == sender) or (prec in receivers)):
                    prec = random.randint(1,4096)
                receivers.append(accts[prec-1]['account'])
                randAmt = random.randint(FEE_NQT,int(0.007*balance))
                amounts.append(randAmt)
                totalToSend = totalToSend + randAmt
            amountInBurst = str(totalToSend / ONE_BURST)
            print(str(sender)+' sends '+amountInBurst+' total Burst to '+str(numReceivers)+' recipients multi_out')
            sendreceipt = send_money_multi(receivers,amounts,'test'+str(sender),random.randint(1,feeUnit)*FEE_NQT)
            tx = sendreceipt['transactionJSON']
            print('Broadcasted: '+str(sendreceipt['broadcasted']))
            fee = int(tx['feeNQT'])/ONE_BURST
            totalfee = totalfee + fee
            print('Fee (Burst): '+str(fee))
            print('Fee Sum (Burst): '+str(totalfee))
            groupTotal = groupTotal + 1
            maxnumberReceivers = max(maxnumberReceivers,numReceivers)
        except:
            logging.exception('error')
            print(sendreceipt)
            
    else:
        print('multi_out_same')
        try:
            balanceresponse = get_balance(senderacct['accountRS'])
            balance = int(balanceresponse['guaranteedBalanceNQT'])
            receivers = []
            totalToSend = 0
            numReceivers = random.randint(12,128)
            for i in range(0,numReceivers):
                prec = random.randint(1,4096)
                while ((prec == sender) or (prec in receivers)):
                    prec = random.randint(1,4096)
                receivers.append(accts[prec-1]['account'])
            randAmt = random.randint(FEE_NQT,int(0.007*balance))
            amountInBurst = str(randAmt / ONE_BURST)
            print(str(sender)+' sends '+str(randAmt)+' Burst to '+str(numReceivers)+' recipients multi_out_same')
            sendreceipt = send_money_multi_same(receivers,randAmt,
                                                'test'+str(sender),
                                                random.randint(1,feeUnit)*FEE_NQT)
            tx = sendreceipt['transactionJSON']
            print('Broadcasted: '+str(sendreceipt['broadcasted']))
            fee = int(tx['feeNQT'])/ONE_BURST
            totalfee = totalfee + fee
            print('Fee (Burst): '+str(fee))
            print('Fee Sum (Burst): '+str(totalfee))
            groupTotal = groupTotal + 1
            maxnumberReceivers = max(maxnumberReceivers,numReceivers)
        except Exception as ex:
            logging.exception('error')
            print(sendreceipt)

    
    time.sleep(1)
    if groupTotal == 100:
        groupTotal = 1
