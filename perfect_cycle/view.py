from fastapi import FastAPI

from perfect_cycle.lib import check_perfect_cycle_batch
from perfect_cycle.model import CheckPerfectCycleRequest, CheckPerfectCycleResponse

app = FastAPI()


@app.post("/check", response_model=CheckPerfectCycleResponse)
async def check_perfect_cycle(request: CheckPerfectCycleRequest):
    output = check_perfect_cycle_batch(input=request.input)
    return CheckPerfectCycleResponse(output=output)
