import logging
import faker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'user.log', level=logging.INFO)

fake = faker.Faker()


def get_user():
    """Generate a single user

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n) -> list[dict[int, str]]:
    """Generate a list of users

    Args:
        n (int): Number of user to generate

    Returns:
        list[dict[int, str]]: users
    """
    logging.info(f"Generating of {n} users.")
    return [{i: get_user()} for i in range(n)]


if __name__ == "__main__":
    users = get_users(5)
    print(users)
