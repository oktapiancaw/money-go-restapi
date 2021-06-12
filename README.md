
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

### [ Method : GET ] - Goals
  Berikut urlnya :
```sh
http://moneygoapi.herokuapp.com/
```
  
  Dan hasil yang akan didapatkan 
```sh
{
  "status" : 200,
  "typeRequest" : "GET"
  "urlRequest" : "http://moneygoapi.herokuapp.com/"
  "message" : "All data has been loaded"
  "data" : [
    {
      "id" : 1,
      "title" : "Target kamu",
      "tags" : "Tags kamu",
      "description" : "lorem ipsum dolor sit amet. "
      "currency_target" : 1000000,
      "end_date" : "2021-01-01",
      "start_date" : "2021-12-31"
    },
    {
      "id" : 2,
      "title" : "Target kamu",
      "tags" : "Tags kamu",
      "description" : "lorem ipsum dolor sit amet. "
      "currency_target" : 1000000,
      "end_date" : "2021-01-01",
      "start_date" : "2021-12-31"
    },
  ]
}
```
