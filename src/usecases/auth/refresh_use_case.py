

from flask_jwt_extended import (
    create_refresh_token,
    get_jwt,
    get_jwt_identity
)



class RefreshUseCase:


    def execute(self):

        current_user_id = get_jwt_identity()
        current_claims = get_jwt()

        
        additional_claims = {
            'username': current_claims.get("username"),
            'email': current_claims.get("email"),
            'sub': 'logistcs-service'
        }
        
        new_access_token = create_refresh_token(
            identity=current_user_id,
            additional_claims=additional_claims
        )

        return {'access_token': new_access_token}