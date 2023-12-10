<!DOCTYPE html>
<html>
<head>
<style>
</style>
    <title>books</title>
</head>
<body>
    <h1>books</h1>
    <a href="/" >Home</a>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>author</th>
        </tr>
        % for book in books:
            <tr>
                <td>{{ book[0] }}</td>
                <td>{{ book[1] }}</td>
                <td>{{ book[2] }}</td>
                <td>
                    <a href="/update_book/{{ book[0] }}">Update</a>
                    <a href="/delete_book/{{ book[0] }}">Delete</a>
                </td>
            </tr>
        % end
    </table>

</body>
</html>
