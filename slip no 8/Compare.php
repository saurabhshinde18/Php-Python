<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
        $largeString = $_POST["large_string"];
        $smallString = $_POST["small_string"];
        $compareChars = $_POST["compare_n_chars"];

        // a. Find whether the small string appears at the start of the large string
        $startsWith = (stripos($largeString, $smallString) === 0) ? "Yes" : "No";

        // b. Find the position of the small string in the big string
        $position = stripos($largeString, $smallString);

        // c. Compare both the strings for the first n characters (case insensitive)
        $substring1 = substr(strtolower($largeString), 0, $compareChars);
        $substring2 = substr(strtolower($smallString), 0, $compareChars);
        $comparisonResult = (strcmp($substring1, $substring2) === 0) ? "Strings match" : "Strings do not match";

        echo "<p>a. Does the small string appear at the start of the large string? Answer: $startsWith</p>";
        echo "<p>b. Position of the small string in the large string: $position</p>";
        echo "<p>c. Comparison of the first $compareChars characters (case insensitive): $comparisonResult</p>";
    }
    ?>