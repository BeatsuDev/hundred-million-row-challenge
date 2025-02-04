use std::{env, fs, process};
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: {} <number>", args[0]);
        process::exit(1);
    }

    let filename = &args[1];

    match fs::read_to_string(filename) {
        Ok(contents) => {
            process_data(contents);
        }
        Err(err) => {
            eprintln!("Error reading file {}: {}", filename, err);
            process::exit(1);
        }
    }
}

struct AggregatePlaceData {
    count: u32,
    min: f64,
    total: f64,
    max: f64
}

struct PlaceData {
    place: String,
    temperature_reading: f64
}

fn process_data(contents: String) {
    let mut aggregate: HashMap<String, AggregatePlaceData> = HashMap::new();
    for line in contents.lines() {
        let data = process_line(line);

        let entry = aggregate.entry(data.place.clone()).or_insert(AggregatePlaceData {
            count: 0,
            min: data.temperature_reading,
            total: 0.0,
            max: data.temperature_reading
        });

        if data.temperature_reading < entry.min {
            entry.min = data.temperature_reading;
        }
        if data.temperature_reading > entry.max {
            entry.max = data.temperature_reading;
        }
        entry.count += 1;
        entry.total += data.temperature_reading;
    }

    for (place, aggregate_data) in aggregate {
        println!("{}", format!("{:>15}:\t{}\t{:.1}\t{}", place, aggregate_data.min, aggregate_data.total / aggregate_data.count as f64, aggregate_data.max));
    }
}

fn process_line(line: &str) -> PlaceData {
    match line.split(";").collect::<Vec<&str>>().as_slice() {
        [place, measurement] => {
            PlaceData { place: place.to_string(), temperature_reading: measurement.parse().unwrap() }
        }
        _ => {
            eprintln!("Could not parse: {}", line);
            process::exit(1);
        }
    }
}