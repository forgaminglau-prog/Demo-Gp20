## Structure 
	S381F-Project-inventory/
	├── server.js  (main server)
	├── package.json
	├── public/    (static files like CSS, JS if needed)
	├── views/     (EJS templates)
	├── models/    (MongoDB schema files if used)
	└── README.md  (project info and instructions)
# Inventory Management System (COMP S381F)
- Group 20 : 
- 13140568
- 13548875
- 13649730
- 13515174
## Description
A simple Inventory Management System using Node.js, Express.js, MongoDB, and EJS. It supports user login/logout, item CRUD operations, and session management.

## Technologies Used
- Node.js
- Express.js
- MongoDB 4.4
- EJS Template Engine
- cookie-session
- body-parser

## Installation and Setup
#### 1. Make sure MongoDB server is installed and running:
    sudo systemctl start mongod
    sudo systemctl enable mongod
#### 2. Clone the project and install dependencies:
    git clone <repository_url>
    cd inventory-management
    npm install
#### 3. Run the server:
    node server.js
#### 4. Access the app in the browser at:
    http://localhost:3000/login

## Usage
- Login with username `admin` and password `password`.
- Add, edit, and delete inventory items.
- Logout using the "Logout" link.

## Notes
- This project uses a hardcoded user for demonstration only.
- For production, implement proper user authentication and password security.


## Test
- This project uses a hardcoded user for demonstration only.
- For production, implement proper user authentication and password security.

Sure! Here's a plain and simple `README.md` version for your GitHub project:

---

# CRUD API Tester

This project tests a RESTful CRUD API deployed on Render.

## API Base URL

```
https://cloud-demo-group-20.onrender.com
```

## Endpoints

- `POST /api/items` — Create a new item  
- `GET /api/items` — Get all items  
- `GET /api/items/:id` — Get item by ID  
- `PUT /api/items/:id` — Update item by ID  
- `DELETE /api/items/:id` — Delete item by ID  

## Python Script

Run `crud_tester.py` to interact with the API:

```
python crud_tester.py
```

Options:
1. Create item (enter name and quantity)
2. Read all items
3. Update item (choose name, quantity, or both)
4. Delete item by ID
5. Search item by ID or name

## cURL Commands

### Create item

```bash
curl -X POST https://cloud-demo-group-20.onrender.com/api/items \
-H "Content-Type: application/json" \
-d '{"name":"Test Item","quantity":1000}'
```

### Read all items

```bash
curl https://cloud-demo-group-20.onrender.com/api/items
```

### Update item

```bash
curl -X PUT https://cloud-demo-group-20.onrender.com/api/items/6913532c2e55e6e194c6e1cb\
-H "Content-Type: application/json" \
-d '{"name":"Banana","quantity":20}'
```

### Delete item

```bash
curl -X DELETE https://cloud-demo-group-20.onrender.com/api/items/{item_id}
```

### Search by ID

```bash
curl https://cloud-demo-group-20.onrender.com/api/items/{item_id}
```

### Search by name (manual filter)

```bash
curl https://cloud-demo-group-20.onrender.com/api/items
```

Then manually check for `"name": "YourName"` in the response.

---

Let me know if you want a Chinese version or want to include login instructions.

