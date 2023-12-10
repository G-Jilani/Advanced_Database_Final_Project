<!DOCTYPE html>
<html>
<head>
    <title>Search Books</title>
</head>
<body>
    <h1>Search Books</h1>
    <a href="/">Home</a>
    <form action="/search_books" method="get">
        <label for="search">Search:</label>
        <input type="text" name="search" placeholder="Enter book name">
        <input type="submit" value="Search">
    </form>

    % if books:
        <table>
            <tr>
                <th>book name</th>
                <th>author</th>
                <th>price</th>
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
    % else:
        <p>No results found for '{{ search_query }}'</p>
    % end
</body>
</html>
