<!DOCTYPE html>
<html>
<head>
    <title>Update Book</title>
</head>
<body>
    <h1>Update Book</h1>
    <a href="/">Home</a>
    <form action="/update_book/{{ books[0] }}" method="post">
        <label for="book_name">Book Name:</label>
        <input type="text" name="book_name" value="{{ books[1] }}" required><br>

        <label for="author">Author:</label>
        <input type="text" name="author" value="{{ books[2] }}" required><br>


        <input type="submit" value="Update Book">
    </form>
</body>
</html>
