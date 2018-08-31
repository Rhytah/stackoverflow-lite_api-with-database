# import unittest
# from api.models.api_models import User 
# from flask_jwt_extended import(JWTManager,jwt_required,create_access_token,get_jwt_identity)


# class TestUserModel(BaseTestCase):


#     def test_encode_auth_token(self):
#         user = User(
#             username='beta',
#             password='test'
#         )
#         db.session.add(user)
#         db.session.commit()
#         auth_token = user.encode_auth_token(user.id)
#         self.assertTrue(isinstance(auth_token, bytes))

# if __name__ == '__main__':
#     unittest.main()