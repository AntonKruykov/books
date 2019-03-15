# Books
For start project run
 
`docker-compose up` or `docker-compose up --buid` for rebuild 


Open [http://0.0.0.0:8080/ui/](http://0.0.0.0:8080/ui/) for Swagger UI page


## Usage

All methods are available on [Swagger UI page](http://0.0.0.0:8080/ui/)

Тo add book in db execute POST on Swagger UI page using content: 

```json
{
  "data": [
    {
      "attributes": {
        "author": "O. Henry",
        "pages_count": 464,
        "publish_year": 1922,
        "title": "Selected stories"
      },
      "type": "books"
    }
  ]
}
```

or execute in shell:
```text
curl -X POST "http://0.0.0.0:8080/books" -H "accept: */*" -H "Content-Type: application/vnd.api+json" -d "{\"data\":[{\"attributes\":{\"author\":\"O. Henry\",\"pages_count\":464,\"publish_year\":1922,\"title\":\"Selected stories\"},\"type\":\"books\"}]}"
```
 
То receive books open link [http://0.0.0.0:8080/books](http://0.0.0.0:8080/books)
 
То filter use [http://0.0.0.0:8080/books?filter[author]=henry&filter[title]=story&filter[date_start]=2019-03-01&filter[date_end]=2019-03-30](http://0.0.0.0:8080/books?filter[author]=henry&filter[title]=story&filter[date_start]=2019-03-01&filter[date_end]=2019-03-30)
