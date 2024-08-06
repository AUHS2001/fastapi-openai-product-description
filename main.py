from fastapi import FastAPI, HTTPException
from utils import generate_description
from schemas import Product

app = FastAPI()

@app.post("/product_description")
async def product_description(product: Product):
    try:
        description = generate_description(f"Product name: {product.name}, Notes: {product.notes}")
        return {"product_description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating description: {str(e)}")