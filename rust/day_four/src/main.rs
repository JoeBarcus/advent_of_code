use std::fs;

fn main() {
    
    let contents = fs::read_to_string("src/input.txt")
        .expect("Cannot read file");

    let parts = contents.split("\n");
    let collection =  parts.collect::<Vec<&str>>();


    // let mut split_camp: Vec<String> = Vec::new();
    let mut overlap_counter = 0;
    for camp in collection {
        let camp_divided = camp.split(",");
        let camp_divided_collect = camp_divided.collect::<Vec<&str>>();

        let split_camp_one = camp_divided_collect[0].split("-");
        let split_camp_one_collect = split_camp_one.collect::<Vec<&str>>();
        let int_camp_one: Vec<i32> = split_camp_one_collect.iter().map(|s| s.parse::<i32>()).collect::<Result<Vec<i32>, _>>().unwrap();

        let split_camp_two = camp_divided_collect[1].split("-");
        let split_camp_two_collect = split_camp_two.collect::<Vec<&str>>();
        let int_camp_two: Vec<i32> = split_camp_two_collect.iter().map(|s| s.parse::<i32>()).collect::<Result<Vec<i32>, _>>().unwrap();

        if int_camp_one[0] >= int_camp_two[0] && int_camp_one[1] <= int_camp_two[1] {
            overlap_counter +=1;
        } else if int_camp_two[0] >= int_camp_one[0] && int_camp_two[1] <= int_camp_one[1] {
            overlap_counter +=1;
        }
    }

    println!("{:?}", overlap_counter)

}
