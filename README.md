
<br />
<p align="center">
  <h3 align="center">Money Go Rest Api</h3>

  <p align="center">
    Sebuah Restfull api untuk mengelola target ataupun keuangan
    <br />
  </p>
</p>

<details open="open">
  <summary>Daftar isi</summary>
  <ol>
    <li><a href="#pendaftaran">Pendaftaran</a></li>
    <li><a href="#penggunaan">Penggunaan</a></li>
  </ol>
</details>

## Pendaftaran
  Untuk melakukan pendaftaran pada aplikasi ini silahkan akses url berikut :
```sh
http://moneygoapi.herokuapp.com/users/
```

  Dengan data sebagai berikut :
```sh
{
  "username" : "username kamu",
  "password" : "password kamu"
}
```
  
## Penggunaan
  Dalam aplikasi ini anda dapat mengelola 2 data yaitu goal dan money sesuai dengan id akun anda, pastikan anda menggunakan basic authentication ketika menkonsumsi API ini

### [ Validation ] - Goals

| Entitas | Tipe data | Panjang | Validasi | Keterangan |
| :---: | :---: | :---: | :---: | :---: | 
| id | Integer | - | required, auto_increment | primary_key |
| title | String | 255 | required, min(4 char), max(255 char) | - |
| tags | String | 100 | required, min(2 char), max(100 char) | - |
| description | String | default | - | - |
| currency_target | Big Integer | default | required, min(1000), max(10000000000) | - |
| start_date | DateTime | deafult | required, min(today) | format(YYYY-mm-dd) |
| end_date | DateTime | deafult | required, min(today) | format(YYYY-mm-dd) |
| created_at | DateTime | deafult | required, min(today) | format(YYYY-mm-dd HH:MM:SS), auto |
| updated_at | DateTime | deafult | required, min(today) | format(YYYY-mm-dd HH:MM:SS), auto |

### [ Method : GET ] - Goals
  Berikut urlnya :
```sh
http://moneygoapi.herokuapp.com/
```
  
  Dan hasil yang akan didapatkan 
```sh
{
   "url": "http://127.0.0.1:5000/goals",
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
      "description": "Membeli hape baru",
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
      "description": "Membeli hape baru",
      "currency_target": 5000000,
      "currency_now": 5000000,
      "status": "finished"
    },
  ]
}
```

  Dan jika terjadi error
```
{
  "type": "GET",
  "url": "http://127.0.0.1:5000/goals",
  "status_code": 404,
  "status": "FAILED",
  "message": "No data in here"
}
```
  
### [ Method : POST ] - Goals
  Berikut urlnya :
```sh
http://moneygoapi.herokuapp.com/
```
  
  Dan hasil yang akan didapatkan 
```sh
{
   "url": "http://127.0.0.1:5000/goals",
  "type": "POST",
  "status_code": 201,
  "status": "SUCCESS",
  "message": "Your data has been created!",
  "data" : [
    {
      "id" : 3,
      "title" : "Target kamu",
      "tags" : "Tags kamu",
      "start_date": "Fri, 01 Jan 2021 00:00:00 -0000",
      "end_date": "Tue, 26 Oct 2021 00:00:00 -0000",
      "description": "Membeli hape baru",
      "currency_target": 5000000,
      "currency_now": 60000,
      "status": "unfinished"
    },
  ]
}
```

  Dan jika terjadi error
```
{
  "type": "POST",
  "url": "http://127.0.0.1:5000/goals",
  "status_code": 400,
  "status": "FAILED",
  "message": "Some validation"
}
```

### [ Method : PATCH ] - Goals
  Berikut urlnya :
```sh
http://moneygoapi.herokuapp.com/goals/id
```
  
  Dan hasil yang akan didapatkan 
```sh
{
   "url": "http://127.0.0.1:5000/goals/id",
  "type": "PATCH",
  "status_code": 201,
  "status": "SUCCESS",
  "message": "The data has been updated!",
  "data" : [
    {
      "id" : 1,
      "title" : "Target Aku",
      "tags" : "Tags kamu",
      "start_date": "Fri, 01 Jan 2021 00:00:00 -0000",
      "end_date": "Tue, 26 Oct 2021 00:00:00 -0000",
      "description": "Membeli hape baru",
      "currency_target": 5000000,
      "currency_now": 60000,
      "status": "unfinished"
    },
  ]
}
```

  Dan jika terjadi error
```
{
  "type": "POST",
  "url": "http://127.0.0.1:5000/goals",
  "status_code": 400,
  "status": "FAILED",
  "message": "Some validation"
}
```

