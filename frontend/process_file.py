import transaction_class as Transaction

#function to process the transaction file
def process_transaction_file(row, accounts, bad_transactions):
    transaction = None
    try:
        transaction = Transaction(
            account_name=row['Account Name'],
            card_num=row['Card Number'],
            trans_amount=row['Transaction Amount'],
            trans_type=row['Transaction Type'],
            description=row['Description'],
            target_card_num=row.get('Target Card Number', None)
        )

        if not transaction.account_name or transaction.card_num:
            bad_transactions.append(transaction)

        #process each type of transaction
        if transaction.trans_type == "Credit":
            accounts[transaction.account_name][transaction.card_num] += transaction.trans_amount
        elif transaction.trans_type == "Debit":
            accounts[transaction.account_name][transaction.card_num] -= transaction.trans_amount
        elif transaction.trans_type == "Transfer" and transaction.target_card_num:
            #check that there is a target card, otherwise add to bad_transaction list to be checked
            if transaction.target_card_num not in accounts[transaction.account_name]:
                bad_transactions.append(row)
            accounts[transaction.account_name][transaction.card_num] -= transaction.trans_amount
            accounts[transaction.account_name][transaction.target_card_num] += transaction.trans_amount
            

    except KeyError:
        bad_transactions.append(transaction)

    return accounts, bad_transactions