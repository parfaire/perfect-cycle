from pydantic import BaseModel


class CheckPerfectCycleRequest(BaseModel):
    input: dict[str, list[int]]

    class Config:
        schema_extra = {
            "example": {
                "input": {
                    "list1": [1, 2, 3],
                    "list2": [0, 2, 5],
                    "list3": [3, 0, 1, 2],
                    "listn": [],
                }
            }
        }


class CheckPerfectCycleResponse(BaseModel):
    output: dict[str, bool]
