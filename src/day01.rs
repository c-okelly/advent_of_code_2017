
fn main() {
    use std::io::prelude::*;
    use std::fs::File;
    use std::str::Split;

    let mut f = File::open("src/day01.txt").expect("File failed to open");

    let mut buffer = String::new();
    f.read_to_string(&mut buffer)
        .expect("Failed to convert file to stirng");

    let splitString = split.collect::<Vec<&buffer>>();
    println!("{}", buffer);

}