<!DOCTYPE html>
<html>
<head>
    <title>String Operations</title>
</head>
<body>
    <h2>String Operations</h2>
    <form method="post">
        <label for="inputString">Enter a string:</label>
        <input type="text" name="inputString" id="inputString" required><br><br>

        <label for="separator">Select a separator:</label>
        <select name="separator" id="separator" required>
            <option value="#">#</option>
            <option value="|">|</option>
            <option value="%">%</option>
            <!-- Add more separator options as needed -->
        </select><br><br>

        <input type="submit" name="submit" value="Submit">
    </form>

    <?php
    if (isset($_POST['submit'])) {
        // Get user input
        $inputString = $_POST['inputString'];
        $selectedSeparator = $_POST['separator'];

        // Task a: Split the string using the selected separator
        $words = explode($selectedSeparator, $inputString);

        // Task b: Replace the separator with a different separator
        $newSeparator = '***'; // Replace with your desired separator
        $replacedString = str_replace($selectedSeparator, $newSeparator, $inputString);

        // Task c: Find the last word in the string
        $lastWord = end($words);

        // Display results
        echo "<h3>Results:</h3>";
        echo "Original String: $inputString<br>";
        echo "Words separated by '$selectedSeparator': " . implode(", ", $words) . "<br>";
        echo "String with separator replaced by '$newSeparator': $replacedString<br>";
        echo "Last Word: $lastWord";
    }
    ?>
</body>
</html>
