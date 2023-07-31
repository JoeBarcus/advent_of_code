use std::fs;

fn main() {

    let contents = fs::read_to_string("src/input.txt")
            .expect("Cannot read file");

    let parts = contents.split("\n");
    let collection = parts.collect::<Vec<&str>>();

    let mut totals: Vec<i32> = Vec::new();
    
    for i in collection {
        let total_play = match_map(i);
        totals.push(total_play);
    }

    let max: i32 = totals.iter().sum();

    println!("{:?}", max)

}


fn match_map(plays: &str) -> i32 {
    match plays {
        // Rock Rock Tie 1 3
        "A X" => 4,
        // Rock Paper Win 2 6
        "A Y" => 8,
        // Rock Scissors Lose 3 0
        "A Z" => 3,
        // Paper Rock Lose 1 0
        "B X" => 1,
        // Paper Paper Tie 2 3
        "B Y" => 5,
        // Paper Scissors Win 3 6
        "B Z" => 9,
        // Scissors Rock Win 1 61
        "C X" => 7,
        // Scissors Paper Lose 2
        "C Y" => 2,
        // Scissors Scissors Tie 3 3
        "C Z" => 6,
        _ => {
            println!("Invalid Input");
            -1
        }
    }
}