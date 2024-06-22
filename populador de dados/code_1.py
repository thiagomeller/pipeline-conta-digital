import json
import random
from datetime import datetime, timedelta
from faker import Faker
from faker.providers import person, address, bank, company, credit_card

fake = Faker('pt_BR')
fake.add_provider(person)
fake.add_provider(address)
fake.add_provider(bank)
fake.add_provider(company)
fake.add_provider(credit_card)

def generate_users(n):
    users = []
    for _ in range(n):
        users.append({
            "person_id": fake.cpf(),
            "username": fake.user_name(),
            "name": fake.name(),
            "created_at": fake.date_time_between(start_date='-3y', end_date='now').isoformat()
        })
    return users

def generate_transactions(n, user_ids):
    transactions = []
    types = ['Pagamento', 'Transferência', 'Depósito']
    for _ in range(n):
        transactions.append({
            "user_id": random.choice(user_ids),
            "created_at": fake.date_time_between(start_date='-3y', end_date='now').isoformat(),
            "type": random.choice(types),
            "description": fake.sentence(nb_words=6),
            "value": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
            "balance_change_type": random.choice(['D', 'C'])
        })
    return transactions

def generate_cards(n, users):
    cards = []
    for _ in range(n):
        user = random.choice(users)
        cards.append({
            "user_id": user["_id"],
            "card_number": fake.credit_card_number(card_type=None),
            "card_holder": user["name"],
            "card_validation_date": fake.date_between(start_date='today', end_date='+3y').isoformat(),
            "card_cvv": fake.random_int(min=100, max=999),
            "card_member_since": fake.date_between(start_date='-3y', end_date='today').isoformat(),
            "card_type": random.choice(['D', 'C'])
        })
    return cards

def generate_bank_accounts(n, user_ids):
    accounts = []
    for _ in range(n):
        accounts.append({
            "user_id": random.choice(user_ids),
            "balance": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
            "credit_limit": round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        })
    return accounts

def generate_applications(n, user_ids):
    applications = []
    types = ['Poupança', 'CDB', 'RDB', 'Fundos de Investimento']
    for _ in range(n):
        applications.append({
            "user_id": random.choice(user_ids),
            "application_type": random.choice(types),
            "value": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
            "interest_rate": round(random.uniform(0.01, 20.00), 2),
            "created_at": fake.date_time_between(start_date='-3y', end_date='now').isoformat()
        })
    return applications

def generate_loans(n, user_ids):
    loans = []
    for _ in range(n):
        initial_date = fake.date_time_between(start_date='-3y', end_date='-1y')
        final_date = initial_date + timedelta(days=365 * random.randint(1, 5))
        loans.append({
            "user_id": random.choice(user_ids),
            "value": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
            "interest_rate": round(random.uniform(0.01, 20.00), 2),
            "installments": random.randint(12, 60),
            "initial_date": initial_date.isoformat(),
            "final_date": final_date.isoformat(),
            "paid": random.choice([True, False])  # Random boolean indicating if loan is paid
        })
    return loans


def save_to_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    n = 10000

    users = generate_users(n)
    for i, user in enumerate(users):
        user["_id"] = i  # Assigning mock _id

    user_ids = [user["_id"] for user in users]

    transactions = generate_transactions(n, user_ids)
    cards = generate_cards(n, users)
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
