from fastapi import Request
from webexteamssdk import WebexTeamsAPI

from app.utils.service_result import ServiceResult

access_token = 'MmZkZTg2MmUtMzBlMy00ZjhmLTgwN2ItMjE1NTczMDVhODUwOGFmN2Q2YzEtZjcy_PF84_0d577422-f7ee-453e-b09d-5bbe97cd69c7'
WEBEX_BOT_USERNAME = 'partediario.vista@webex.bot'


class GithubbotService():
    def listener(request: Request) -> ServiceResult:

        print("\ndentro GithubotService().listener\n")
        api = WebexTeamsAPI(access_token = access_token)

        #print("\ndentro del POST webexBot v1/tlogic/vista/parte_diario")
        headers = request.headers
        body = request.json()
        print(type(body))
        #body = json.dumps(body)
        print('\nwebexBot :: HEADER >> {}'.format(headers))
        print('\nwebexBot :: BODY >> {}'.format(body))
        data_id = body["data"]["id"]
        room_id = body["data"]["roomId"]

        response = room_id
                
        return ServiceResult(response)
