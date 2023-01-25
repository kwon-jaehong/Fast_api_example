from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/")
async def upload( request: Request):
    request_body = await request.form()
    # request.state.body = request_body
    print(request_body)

    return {"message": f"Successfuly uploaded "} 