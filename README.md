# Smart Home API

This FastAPI-based Smart Home API provides CRUD operations for managing Users, Devices, Rooms, and Houses.


## **API Data Structures**
### **User**
- `id` (str) - Unique user ID (auto-generated if not provided)
- `name` (str) - User’s full name
- `phone_number` (str) - User’s phone number (XXXXXXXXXX format)
- `email` (str) - User’s email address


### **Device**
- `id` (str) - Unique device ID (auto-generated if not provided)
- `name` (str) - Device name
- `type` (str) - Device type (e.g., TV, Thermometer)
- `room_id` (str) - ID of the room the device belongs to

### **Room**
- `id` (str) - Unique room ID (auto-generated if not provided)
- `name` (str) - Room name
- `type` (str) - Room type (e.g., bedroom, kitchen)
- `size` (float) - Room size in square feet
- `house_id` (str) - ID of the house the room belongs to

### **House**
- `id` (str) - Unique house ID (auto-generated if not provided)
- `name` (str) - House name
- `address` (str) - House address
- `owners` (list of str) - List of owner IDs
- `occupants` (list of str) - List of occupant IDs


## **API Functions**
### **Users**
| Method  | Path                | Function Name    | Description |
|---------|---------------------|-----------------|-------------|
| `POST`  | `/users`            | `create_user`   | Create a user |
| `GET`   | `/users/{user_id}`   | `get_user`      | Retrieve a user by ID |
| `PUT`   | `/users/{user_id}`   | `update_user`   | Update a user|
| `DELETE`| `/users/{user_id}`   | `delete_user`   | Delete a user by ID |

### **Devices**
| Method  | Path                | Function Name    | Description |
|---------|---------------------|-----------------|-------------|
| `POST`  | `/devices`          | `create_device` | Create a device |
| `GET`   | `/devices/{device_id}` | `get_device` | Retrieve a device by ID |
| `PUT`   | `/devices/{device_id}` | `update_device` | Update a device |
| `DELETE`| `/devices/{device_id}` | `delete_device` | Delete a device by ID |

### **Rooms**
| Method  | Path                | Function Name    | Description |
|---------|---------------------|-----------------|-------------|
| `POST`  | `/rooms`            | `create_room`   | Create a room |
| `GET`   | `/rooms/{room_id}`   | `get_room`      | Retrieve a room by ID |
| `PUT`   | `/rooms/{room_id}`   | `update_room`   | Update a room |
| `DELETE`| `/rooms/{room_id}`   | `delete_room`   | Delete a room by ID |

### **Houses**
| Method  | Path                | Function Name    | Description |
|---------|---------------------|-----------------|-------------|
| `POST`  | `/houses`           | `create_house`  | Create a house |
| `GET`   | `/houses/{house_id}` | `get_house`     | Retrieve a house by ID |
| `PUT`   | `/houses/{house_id}` | `update_house`  | Update a house |
| `DELETE`| `/houses/{house_id}` | `delete_house`  | Delete a house by ID|