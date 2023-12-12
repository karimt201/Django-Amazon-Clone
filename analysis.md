Products
  data :
    - name
    - flag (new , sale,feature)
    - price
    - images
    - reviews :
        - name
        - image
        - review
        - rate
        - date
    - reviews count
    - brand :
        - name
        - image 
        - item count
    - sku 
    - subtitle
    - tags
    - related
    - description

    classes :
        - product
            - brand
            - description
        - review
            - product
        - brand


        - image



  function:
    - list
    - detail
    - brand list
    - brand detail
    - search
    - filter
    - add to cart
    - add to wishlist


Users :
  data :
    - username
    - email
    - image
    - contact numbers :
        - type (primary , secondery)
        - number
    - address :
        - type : (home , office , bussines , academy , other)
        - address

     



  Functions :
    - auth
    - dashboard
    - profile
    - edit profile 
