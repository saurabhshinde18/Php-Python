<!DOCTYPE html>
<html>
<head>
    <style>
        /* Define styles for the chessboard */
        .chessboard {
            width: 400px;
            height: 400px;
            border-collapse: collapse;
        }

        .chessboard td {
            width: 50px;
            height: 50px;
            text-align: center;
            vertical-align: middle;
            font-size: 24px;
        }

        /* Define alternating cell styles for the checkerboard pattern */
        .chessboard .even {
            background-color: #f0d9b5; /* Light color */
        }

        .chessboard .odd {
            background-color: #b58863; /* Dark color */
        }
    </style>
</head>
<body>
    <table class="chessboard">
        <?php
        // Loop to generate the chessboard pattern
        for ($row = 1; $row <= 8; $row++) {
            echo "<tr>";
            for ($col = 1; $col <= 8; $col++) {
                $cell_class = ($row + $col) % 2 == 0 ? "even" : "odd";
                echo "<td class='$cell_class'></td>";
            }
            echo "</tr>";
        }
        ?>
    </table>
</body>
</html>
