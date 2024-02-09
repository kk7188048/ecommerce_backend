from fastapi import FastAPI
import uvicorn


from app.api.product import router as product_routes
from app.api.user import router as user_routes
from app.api.order import router as order_routes

app = FastAPI()

# Include routers
app.include_router(product_routes.router)
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(order_routes.router, prefix="/orders", tags=["orders"])

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
