from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# from app.routes import users
from fastapi.exceptions import RequestValidationError

# from app.routes import db_connection, fe_configs, fe_data_loader, fe_preprocessing, feature_selection, feature_engineering
from routes import classifier

app = FastAPI()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def healthcheck():
    return {"message": "running"}


app.include_router(classifier.router)


# app.include_router(oa_configs.router)
# app.include_router(oa_data_loader.router)
# app.include_router(oa_apply_cg.router)
# app.include_router(oa_leads_assignment.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
