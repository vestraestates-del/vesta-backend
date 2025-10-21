from fastapi import FastAPI
from database import engine, Base
from routers import auth, portfolio, vault, invites

# create DB tables (only for simple setup; in production use migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title='VestaEstates Backend (Render)')

app.include_router(invites.router, prefix='/api/invites', tags=['invites'])
app.include_router(auth.router, prefix='/api/auth', tags=['auth'])
app.include_router(portfolio.router, prefix='/api/properties', tags=['properties'])
app.include_router(vault.router, prefix='/api/vault', tags=['vault'])

@app.get('/')
def root():
    return {'message': 'VestaEstates Backend is running'}
