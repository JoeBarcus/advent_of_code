use std::fs;

fn main() {
    // Read in the file
    let contents = fs::read_to_string("src/input.txt")
        .expect("cannot read file");

    // Convert file string contents into a vector of strings
    let parts = contents.split("\n");
    let collection = parts.collect::<Vec<&str>>();

    let mut sum_list: Vec<i32> = Vec::new();
    let mut totals: Vec<i32> = Vec::new();

    for i in collection {
        let new_line: &str = "";

        if i != new_line {
            let integer: i32 = i.parse().unwrap();
            sum_list.push(integer.clone());
        }
        else {
            let sum: i32 = sum_list.iter().sum();
            totals.push(sum.clone());
            sum_list.clear();
        }
    }

    let max_one: i32 = *totals.iter().max().unwrap();
    println!("{:?}", max_one);
    let index_one = totals.iter().position(|&x| x == max_one).unwrap();
    totals.remove(index_one);

    let max_two: i32 = *totals.iter().max().unwrap();
    let index_two = totals.iter().position(|&x| x == max_two).unwrap();
    totals.remove(index_two);

    let max_three: i32 = *totals.iter().max().unwrap();

    let grand_total = max_one + max_two + max_three;

    println!("{:?}", grand_total);
}

