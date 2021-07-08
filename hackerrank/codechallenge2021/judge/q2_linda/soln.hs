import Data.List -- for transpose

-- wordsWhen copied from stackoverflow.com
wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

-- Not the most efficient, but gets the job done.
barText :: Int -> Int -> String
barText maxlen n = (replicate (maxlen-n) ' ') ++ (replicate n '+')

solve :: [[Int]] -> [String]
solve s = map ((barText.maximum.concat) s) (map maximum (transpose s))

main = interact $ unlines . transpose . solve . map (map read . wordsWhen (==',')) . lines

-- (putStrLn . show) (1 + 1) = putStrLn . show $ 1 + 1 = putStrLn (show (1 + 1))
-- (f . g) x = f (g x)
-- transpose s = transpose(s)

-- countNeg :: [[Int]] -> Int
-- countNeg = length . filter (<0) . concat
