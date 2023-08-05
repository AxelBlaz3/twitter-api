from abc import ABC
from typing import Optional

from app.user.domain.models.user import User, UserUpdate

class UserRepository(ABC):
    async def get_user(id: str) -> Optional[User] | None:
        """
        Fetches a user from the database by their ID.

        Args:
            id (str): The unique identifier of the user.

        Returns:
            Optional[User] or None: If a user with the given ID is found, returns a User object.
                                    If no user is found with the given ID, returns None.
        """
        pass

    async def update_user(id: int, user_update: UserUpdate) -> int:
        """
        Updates an existing user in the database with the provided data.

        Args:
            id (int): The unique identifier of the user to be updated.
            user_update (UserUpdate): An object containing the updated user data.

        Returns:
            int: The number of rows affected in the database (usually 1 if the update was successful).
        """
        pass

    async def new_follower(user_id: str, follower_id: str) -> int:
        """
        Adds a new follower to the user.

        Args:
            user_id (str): The unique identifier of the user.
            follower_id (str): The unique identifier of the follower.

        Returns:
            int: The number of rows affected in he database.
        """
        pass

    async def remove_follower(user_id: str, follower_id: str) -> int:
        """
        Removes an existing follower of a user.

        Args:
            user_id (str): The unique identifier of the user.
            follower_id (str): The unique identifier of the follower.

        Returns:
            int: The number of rows affected in he database.
        """
        pass
