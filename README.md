
<br />
<p align="center">
  <h3 align="center">Money Go Rest Api</h3>

  <p align="center">
    Sebuah Restfull api untuk mengelola target ataupun keuangan
    <br />
  </p>
</p>

- [Pendaftaran](#pendaftaran)
- [Penggunaan](#penggunaan)
- [Goal](#goal)
  - [Entitas & Keterangan data](#entitas--keterangan-data)
  - [[ Method : GET ] - Get all goals](#-method--get----get-all-goals)
  - [[ Method : POST ] - Add a goal](#-method--post----add-a-goal)
  - [[ Method : PATCH ] - Edit a goal](#-method--patch----edit-a-goal)
  - [[ Method : GET ] - Get a specific goal](#-method--get----get-a-specific-goal)
  - [[ Method : DELETE ] - Delete a goal](#-method--delete----delete-a-goal)
- [Manage](#manage)
  - [Entitas & Keterangan data](#entitas--keterangan-data-1)
  - [[ Method : GET ] - Get all manages](#-method--get----get-all-manages)
  - [[ Method : POST ] - Add a manage](#-method--post----add-a-manage)
  - [[ Method : GET ] - Get a specific goal](#-method--get----get-a-specific-goal-1)
  - [[ Method : DELETE ] - Delete a goal](#-method--delete----delete-a-goal-1)

<br/><br/>
## Pendaftaran
<hr/>
  Untuk melakukan pendaftaran pada aplikasi ini silahkan akses url berikut :

```json
http://moneygoapi.herokuapp.com/users
```

  Dengan data sebagai berikut :
```json
{
  "username" : "username kamu",
  "password" : "password kamu"
}
```

<br/><br/>
## Penggunaan
<hr/>
  Dalam aplikasi ini anda dapat mengelola 2 data yaitu goal dan money sesuai dengan id akun anda, pastikan anda menggunakan basic authentication ketika menkonsumsi API ini

  Dengan basic auth sebagai berikut :
```json
{
  "username" : "username kamu",
  "password" : "password kamu"
}
```
<br/><br/>

## Goal
<hr/>

  Berikut contohdefault raw data yang harus di kirimkan :
```json
{
    "title" : "Target kamu",
    "tags" : "Tags kamu",
    "start_date": "2021-01-01",
    "end_date": "2021-10-26",
    "description": "Keterangan dari goal ini",
    "currency_target": 5000000
}
```

### Entitas & Keterangan data
<hr/>

| Entitas | Tipe data | Panjang | Validasi | Keterangan |
| --- | :---: | :---: | :---: | :---: | 
| id | Integer | - | required, auto_increment | primary_key |
| title | String | 255 | required, min(4 char), max(255 char) | - |
| tags | String | 100 | required, min(2 char), max(100 char) | - |
| description | String | default | - | - |
| currency_target | Big Integer | default | required, min(1000), max(10000000000) | - |
| start_date | DateTime | deafult | required, min(today) | format(YYYY-mm-dd) |
| end_date | DateTime | deafult | required, min(today) | format(YYYY-mm-dd) |
| created_at | DateTime | deafult | required, min(today) | format(YYYY-mm-dd HH:MM:SS), auto |
| updated_at | DateTime | deafult | required, min(today) | format(YYYY-mm-dd HH:MM:SS), auto |

<br/>
<br/>

### [ Method : GET ] - Get all goals
<hr/>

  Berikut contoh urlnya :
```json
http://moneygoapi.herokuapp.com/goals
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/goals",
  "type": "GET",
  "status_code": 200,
  "status": "SUCCESS",
  "message": "All data has been loaded",
  "data" : [
    {
      "id" : 1,
      "title" : "Target kamu",
      "tags" : "Tags kamu",
      "start_date": "Fri, 01 Jan 2021 00:00:00 -0000",
      "end_date": "Tue, 26 Oct 2021 00:00:00 -0000",
      "description": "Keterangan dari goal ini",
      "currency_target": 5000000,
      "currency_now": 60000,
      "status": "unfinished"
    },
    {
      "id" : 2,
      "title" : "Target kamu",
      "tags" : "Tags kamu",
      "start_date": "Fri, 01 Jan 2021 00:00:00 -0000",
      "end_date": "Tue, 26 Oct 2021 00:00:00 -0000",
      "description": "Keterangan dari goal ini",
      "currency_target": 5000000,
      "currency_now": 5000000,
      "status": "finished"
    },
  ]
}
```

  Dan jika terjadi error
```json
{
  "type": "GET",
  "url": "http://moneygoapi.herokuapp.com/goals",
  "status_code": 404,
  "status": "FAILED",
  "message": "No data in here"
}
```
<br/><br/>  
### [ Method : POST ] - Add a goal

<hr/>

  Berikut contoh urlnya :

```json
http://moneygoapi.herokuapp.com/
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/goals",
  "type": "POST",
  "status_code": 201,
  "status": "SUCCESS",
  "message": "Your data has been created!",
  "data" : {
      "id" : 3,
      "title" : "Target kamu",
      "tags" : "Tags kamu",
      "start_date": "Fri, 01 Jan 2021 00:00:00 -0000",
      "end_date": "Tue, 26 Oct 2021 00:00:00 -0000",
      "description": "Keterangan dari goal ini",
      "currency_target": 5000000,
      "currency_now": 60000,
      "status": "unfinished"
    },
}
```

  Dan jika terjadi error
```json
{
  "type": "POST",
  "url": "http://moneygoapi.herokuapp.com/goals",
  "status_code": 400,
  "status": "FAILED",
  "message": "Some validation"
}
```
<br/><br/>  

### [ Method : PATCH ] - Edit a goal
  Berikut contoh urlnya :
```json
http://moneygoapi.herokuapp.com/goals/id
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/goals/id",
  "type": "PATCH",
  "status_code": 201,
  "status": "SUCCESS",
  "message": "The data has been updated!",
  "data" : {
      "id" : 1,
      "title" : "Target Aku",
      "tags" : "Tags kamu",
      "start_date": "Fri, 01 Jan 2021 00:00:00 -0000",
      "end_date": "Tue, 26 Oct 2021 00:00:00 -0000",
      "description": "Keterangan dari goal ini",
      "currency_target": 5000000,
      "currency_now": 60000,
      "status": "unfinished"
    },
}
```

  Dan jika terjadi error
```json
{
  "type": "PATCH",
  "url": "http://moneygoapi.herokuapp.com/goals/1",
  "status_code": 400,
  "status": "FAILED",
  "message": "Some validation"
}
```
<br/><br/>  

### [ Method : GET ] - Get a specific goal
<hr/>

  Berikut contoh urlnya :
```json
http://moneygoapi.herokuapp.com/goals/1
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/goals/1",
  "type": "GET",
  "status_code": 200,
  "status": "SUCCESS",
  "message": "The data is founded",
  "data" : {
      "id" : 1,
      "title" : "Target kamu",
      "tags" : "Tags kamu",
      "start_date": "Fri, 01 Jan 2021 00:00:00 -0000",
      "end_date": "Tue, 26 Oct 2021 00:00:00 -0000",
      "description": "Keterangan dari goal ini",
      "currency_target": 5000000,
      "currency_now": 60000,
      "status": "unfinished"
    }
}
```

  Dan jika terjadi error
```json
{
  "type": "GET",
  "url": "http://moneygoapi.herokuapp.com/goals/1",
  "status_code": 404,
  "status": "FAILED",
  "message": "Data isn't exist!"
}
```
<br/><br/>  


### [ Method : DELETE ] - Delete a goal
<hr/>

  Berikut contoh urlnya :
```json
http://moneygoapi.herokuapp.com/goals/1
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/goals/1",
  "type": "DELETE",
  "status_code": 204,
  "status": "SUCCESS",
  "message": "Data has been deleted!",
}
```

  Dan jika terjadi error
```json
{
  "type": "DELETE",
  "url": "http://moneygoapi.herokuapp.com/goals/1",
  "status_code": 404,
  "status": "FAILED",
  "message": "Data isn't exist!"
}
```
<br/><br/>  

## Manage

  Berikut contohdefault raw data yang harus di kirimkan :
```json
{
  "goal_id" : 1,
  "nominal" : 100,
  "date" : "2021-01-05",
  "status": 1
}
```

### Entitas & Keterangan data
<hr/>

| Entitas | Tipe data | Panjang | Validasi | Keterangan |
| --- | :---: | :---: | :---: | :---: | 
| id | Integer | - | required, auto_increment | primary_key, auto |
| goal_id | Integer | - | required | foreign_key(goals) |
| nominal | Big Integer | default | required, min(1000), max(10000000000) | - |
| date | DateTime | deafult | required, min(today) | format(YYYY-mm-dd) |
| status | Integer | - | enum(0,1,2) | default=0 |
<br/><br/>  
### [ Method : GET ] - Get all manages
<hr/>

  Berikut contoh urlnya :
```json
http://moneygoapi.herokuapp.com/manages
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/manages",
  "type": "GET",
  "status_code": 200,
  "status": "SUCCESS",
  "message": "All data has been loaded",
  "data" : [
    {
      "id": 1,
      "goal_id": 1,
      "nominal": 50000,
      "date": "Sat, 02 Jan 2021 00:00:00 -0000",
      "status": 1
    },
    {
      "id": 2,
      "goal_id": 1,
      "nominal": 60000,
      "date": "Sun, 03 Jan 2021 00:00:00 -0000",
      "status": 1
    },
    {
      "id": 3,
      "goal_id": 2,
      "nominal": 60000,
      "date": "Sun, 03 Jan 2021 00:00:00 -0000",
      "status": 1
    },
    {
      "id": 4,
      "goal_id": 1,
      "nominal": 4890000,
      "date": "Mon, 04 Jan 2021 00:00:00 -0000",
      "status": 1
    }
  ]
}
```

  Dan jika terjadi error
```json
{
  "type": "GET",
  "url": "http://moneygoapi.herokuapp.com/manages",
  "status_code": 404,
  "status": "FAILED",
  "message": "No data in here"
}
```
<br/><br/>  
### [ Method : POST ] - Add a manage

<hr/>

  Berikut contoh urlnya :

```json
http://moneygoapi.herokuapp.com/
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/manages",
  "type": "POST",
  "status_code": 201,
  "status": "SUCCESS",
  "message": "Your data has been created!",
  "data" : {
      "id": 5,
      "goal_id": 2,
      "nominal": 43000,
      "date": "Mon, 04 Jan 2021 00:00:00 -0000",
      "status": 1
    }
}
```

  Dan jika terjadi error
```json
{
  "type": "POST",
  "url": "http://moneygoapi.herokuapp.com/manages",
  "status_code": 400,
  "status": "FAILED",
  "message": "Some validation"
}
```
<br/><br/>  

### [ Method : GET ] - Get a specific goal
<hr/>

  Berikut contoh urlnya :
```json
http://moneygoapi.herokuapp.com/manages/5
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/manages/5",
  "type": "GET",
  "status_code": 200,
  "status": "SUCCESS",
  "message": "The data is founded",
  "data" : {
      "id": 5,
      "goal_id": 2,
      "nominal": 43000,
      "date": "Mon, 04 Jan 2021 00:00:00 -0000",
      "status": 1
    }
}
```

  Dan jika terjadi error
```json
{
  "type": "GET",
  "url": "http://moneygoapi.herokuapp.com/manages/5",
  "status_code": 404,
  "status": "FAILED",
  "message": "Data isn't exist!"
}
```
<br/><br/>  


### [ Method : DELETE ] - Delete a goal
<hr/>

  Berikut contoh urlnya :
```json
http://moneygoapi.herokuapp.com/manages/5
```
  
  Dan hasil yang akan didapatkan 
```json
{
   "url": "http://moneygoapi.herokuapp.com/manages/5",
  "type": "DELETE",
  "status_code": 204,
  "status": "SUCCESS",
  "message": "Data has been deleted!",
}
```

  Dan jika terjadi error
```json
{
  "type": "DELETE",
  "url": "http://moneygoapi.herokuapp.com/manages/5",
  "status_code": 404,
  "status": "FAILED",
  "message": "Data isn't exist!"
}
```
<br/><br/>  