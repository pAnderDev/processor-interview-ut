import streamlit as st
import pandas as pd

#transaction class objects

class Transaction:
    def __init__(self, account_name, card_num, trans_amount, trans_type, description, target_card_num):
        self.account_name = account_name
        self.card_num = card_num
        self.trans_amount = trans_amount
        self.trans_type = trans_type
        self.description = description
        self.target_card_num = target_card_num