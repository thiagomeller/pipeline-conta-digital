import json
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_users(n):
    users = []
    for i in range(n):
        users.append({
            "id": i + 1,
            "person_id": fake.random_int(min=1, max=n),
            "username": fake.user_name(),
            "created_at": fake.date_time_between(start_date='-3y', end_date='now').isoformat()
        })
    return users

def generate_transactions(n, user_ids):
    transactions = []
    types = ['type1', 'type2', 'type3']
    for i in range(n):
        transactions.append({
            "id": i + 1,
            "user_id": random.choice(user_ids),
            "created_at": fake.date_time_between(start_date='-3y', end_date='now').isoformat(),
            "type": random.choice(types),
            "description": fake.text(max_nb_chars=50),
            "value": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
            "balance_change_type": random.choice(['D', 'C'])
        })
    return transactions

def generate_cards(n, user_ids):
    cards = []
    for i in range(n):
        cards.append({
            "id": i + 1,
            "user_id": random.choice(user_ids),
            "card_number": fake.credit_card_number(),
            "card_holder": fake.name(),
            "card_validation_date": fake.date_between(start_date='today', end_date='+3y').isoformat(),
            "card_cvv": fake.random_int(min=100, max=999),
            "card_member_since": fake.date_between(start_date='-3y', end_date='today').isoformat(),
            "card_type": random.choice(['D', 'C'])
        })
    return cards

def generate_bank_accounts(n, user_ids):
    accounts = []
    for i in range(n):
        accounts.append({
            "id": i + 1,
            "user_id": random.choice(user_ids),
            "balance": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
            "credit_limit": round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        })
    return accounts

def generate_applications(n, user_ids):
    applications = []
    for i in range(n):
        applications.append({
            "id": i + 1,
            "user_id": random.choice(user_ids),
            "application_type": random.choice(['S', 'T']),
            "value": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
            "interest_rate": round(random.uniform(0.01, 20.00), 2),
            "created_at": fake.date_time_between(start_date='-3y', end_date='now').isoformat()
        })
    return applications

def generate_loans(n, user_ids):
    loans = []
    for i in range(n):
        initial_date = fake.date_time_between(start_date='-3y', end_date='-1y')
        final_date = initial_date + timedelta(days=365 * random.randint(1, 5))
        loans.append({
            "id": i + 1,
            "user_id": random.choice(user_ids),
            "value": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
            "interest_rate": round(random.uniform(0.01, 20.00), 2),
            "installments": random.randint(12, 60),
            "initial_date": initial_date.isoformat(),
            "final_date": final_date.isoformat()
        })
    return loans

def save_to_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    n = 10000

    users = generate_users(n)
    user_ids = [user["id"] for user in users]

    transactions = generate_transactions(n, user_ids)
    cards = generate_cards(n, user_ids)
    bank_accounts = generate_bank_accounts(n, user_ids)
    applications = generate_applications(n, user_ids)
    loans = generate_loans(n, user_ids)

    save_to_json('users.json', users)
    save_to_json('transactions.json', transactions)
    save_to_json('cards.json', cards)
    save_to_json('bank_accounts.json', bank_accounts)
    save_to_json('applications.json', applications)
    save_to_json('loans.json', loans)

if __name__ == "__main__":
    main()
