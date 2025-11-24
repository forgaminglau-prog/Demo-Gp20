# Part 1. Project info
# Inventory Management System (COMP S381F)
- Group 20 : 
- 13140568 Yu Ching Ting
- 13548875 Lau Wai Shun
- 13649730 Chung Ka Yuet
- 13515174 Kan Tsz Hong Michael
## Description
A simple Inventory Management System using Node.js, Express.js, MongoDB, and EJS. It supports user login/logout, item CRUD operations, and session management.

# Part 2. Project file intro
## Structure 
	S381F-Project-inventory/
	├── server.js  (main server)
	├── package.json
	├── public/    (static files like CSS, JS if needed)
	├── views/     (EJS templates)
	└── README.md  (project info and instructions)
## server.js provide main function 
- Main function
- Login/Logout , CRUD Page , RESTful API
- Connect to MongoDB

## Technologies Used (dependencies)
- Node.js
- Express.js
- MongoDB 4.4
- EJS Template Engine
- cookie-session
- body-parser

## /views folder
- add.ejs: Page for adding new inventory items

- edit.ejs: Page for editing existing inventory items

- index.ejs: Main page displaying the full inventory list

- login.ejs: User login interface

# Part 3. Cloud-based server URL
## Cloud-based server URL
- https://cloud-demo-group-20.onrender.com/

# Part 4. Operation guides 
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

## Operation guides 
- **Login/Logout pages** 
	- Login with username `admin` and password `password`.
	  <img width="749" height="379" alt="image" src="https://github.com/user-attachments/assets/d3db16b5-3488-46fb-ad09-7843ec7c375a" />
	- Logout using the "Logout" button.
- **CRUD web pages**
	- Inventory List (Read/Search/Edit/Delete inventory item )
	  <img width="914" height="357" alt="image" src="https://github.com/user-attachments/assets/b4f8a6f7-69b2-47fb-b6fb-fceca475eda3" />
	- Add /Random generate inventory items.
	  <img width="930" height="363" alt="image" src="https://github.com/user-attachments/assets/5b906195-9b0c-4c29-9b30-f402c4308d3b" />
- **Example** 
	<img width="915" height="828" alt="image" src="https://github.com/user-attachments/assets/747def83-2c32-45ac-b9bb-f41d771f3494" />







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

## CURL Commands

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
curl -X PUT https://cloud-demo-group-20.onrender.com/api/items/{item_id}\
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



---


