<!DOCTYPE html>
<html>
<head>
    <title>Price</title>
</head>
<body>
    <h1>price</h1>
    <a href="/">Home</a>
    <table border="1">
        <tr>
            <th>Price ID</th>
            <th>Book id</th>
            <th>Price</th>
        </tr>
        % for price in price:
            <tr>
                <td>{{ price[0] }}</td>
                <td>{{ price[1] }}</td>
		<td>{{ price[2] }}</td>
            </tr>
        % end
    </table>
</body>
</html>
