## Setting a variable
- Using `SET`
```sql
SET @variable_name = value;
```
- Using the `:=` operator
```sql
SELECT @variable_name := value;
```

## Using a variable
```sql
SELECT @variable_name;
```
