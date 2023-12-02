use std::fs;
use std::collections::{HashMap, HashSet};

fn main() {

    let letters: Vec<char> = letters();
    let numbers: Vec<i32> = numbers();
    let mappings: HashMap<char, i32> = letters.into_iter().zip(numbers.into_iter()).collect();

    let contents = fs::read_to_string("src/input.txt")
        .expect("Cannot read file");
    let parts = contents.split("\n");
    let collection = parts.collect::<Vec<&str>>();
    

    let mut rucksacks: Vec<(&str, &str)> = Vec::new();
    for i in collection.clone() {
        let midpoint: usize = i.len() / 2;
        let end: usize = i.len();
        
        let first_rucksack = &i[0..midpoint];
        let second_rucksack: &str = &i[midpoint..end];
        rucksacks.push((first_rucksack, second_rucksack));
    }    

    let mut common_items: Vec<&i32> = Vec::new();
    for (ruck_one, ruck_two) in rucksacks {
        let set1: HashSet<_> = ruck_one.chars().collect();
        let set2: HashSet<_> = ruck_two.chars().collect();

        let duplicate_items: HashSet<&char> = set1.intersection(&set2).collect();
        let duplicate_char: &char = duplicate_items.iter().next().unwrap();
        let mapping_value: &i32 = mappings.get(duplicate_char).unwrap();
        common_items.push(mapping_value);
        
    }

    let total: i32 = common_items.iter().map(|&x| x).sum();
    println!("{}", total);



    /////////////////  Part 2  /////////////////
    
    let mut letter_value: Vec<&i32> = Vec::new();


    for ruck in collection.chunks(3) {
        let ruck_one: HashSet<_> = ruck[0].chars().collect();
        let ruck_two: HashSet<_> = ruck[1].chars().collect();
        let ruck_three: HashSet<_> = ruck[2].chars().collect();
        
        let common_letters = ruck_one.intersection(&ruck_two).cloned().collect::<HashSet<char>>().intersection(&ruck_three).cloned().collect::<HashSet<char>>();
        let char_conversion = *common_letters.iter().next().unwrap();
        let mapping_value: &i32 = mappings.get(&char_conversion).unwrap();
        
        letter_value.push(mapping_value)

    }

    let total_part_two: i32 = letter_value.iter().map(|&x| x).sum();
    println!("{:?}", total_part_two);

    }





pub fn letters() -> Vec<char> {

    let mut letters: Vec<char> = Vec::new();

    for ch in 'a'..='z' {
        letters.push(ch)
    }

    for ch in 'a'..='z' {
        letters.push(ch.to_uppercase().next().unwrap())
    }

    letters
}

pub fn numbers() -> Vec<i32> {
    
    let mut numbers: Vec<i32> = Vec::new();

    for num in 1..=52 {
        numbers.push(num);
    }

    numbers
}


