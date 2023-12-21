// Name: Irhan Iftikar
// Date: October 2023
// Description: Locally hosted website that calculates postage cost given inputs. Script.js runs back-end cost calculations
// Challenges: Advanced UI, rounds outputs to two decimals, accounts for user errors, removes leading '0' if output is less than 1
// Bugs: None found
// Sources: Various Internet syntax sources (StackOverflow, w3schools, etc.)

// Function takes inputs from index.html and returns them as JS variables
function take_input() {
    var length = document.getElementById("length").value
    var height = document.getElementById("height").value
    var thickness = document.getElementById("thickness").value
    var start_zip = document.getElementById("start_zip").value
    var end_zip = document.getElementById("end_zip").value
    return [length, height, thickness, start_zip, end_zip]
}

// Function takes in length, height, and thickness parameters and returns the package type
function classify_package(length, height, thickness) {
    var distance = 2*length + 2*height + 2*thickness
    if (length >= 3.5 && length <= 4.25 && height >= 3.5 && height <= 6 && thickness >= 0.007 && thickness <= 0.016) {
        var package = "Regular Post Card"
      } else if (length >= 4.25 && length <= 6 && height >= 6 && height <= 11.5 && thickness >= 0.007 && thickness <= 0.015) {
        var package =  "Large Post Card"
      } else if (length >= 3.5 && length <= 6.125 && height >= 5 && height <= 11.5 && thickness >= 0.016 && thickness <= 0.25) {
        var package =  "Envelope"
      } else if (length >= 6.125 && length <= 24 && height >= 11 && height <= 18 && thickness >= 0.25 && thickness <= 0.5) {
        var package =  "Large Envelope"
      } else if (length > 0 && height > 0 && thickness > 0 && distance >= 0 && distance <= 84) {
        var package =  "Package"
      } else if (length > 0 && height > 0 && thickness > 0 && distance > 84 && distance <= 130) {
        var package = "Large Package"
      }
        else {
        var package = "Unmailable"
      }
    return package
}

// Function takes in start and ending zip codes and returns total zones the package passes through
function classify_zone(start_zip, end_zip) {
    if (1 <= start_zip && start_zip <= 6999) {
        var start_zone = 1
    }   else if (7000 <= start_zip && start_zip <= 19999) {
        var start_zone = 2
    }   else if (20000 <= start_zip && start_zip <= 35999) {
        var start_zone = 3
    }   else if (36000 <= start_zip && start_zip <= 62999) {
        var start_zone = 4
    }   else if (63000 <= start_zip && start_zip <= 84999) {
        var start_zone = 5
    }   else if (85000 <= start_zip && start_zip <= 99999) {
        var start_zone = 6
    }   else {
        var start_zone = "Unmailable"
    }
    if (1 <= end_zip && end_zip <= 6999) {
        var end_zone = 1
    }   else if (7000 <= end_zip && end_zip <= 19999) {
        var end_zone = 2
    }   else if (20000 <= end_zip && end_zip <= 35999) {
        var end_zone = 3
    }   else if (36000 <= end_zip && end_zip <= 62999) {
        var end_zone = 4
    }   else if (63000 <= end_zip && end_zip <= 84999) {
        var end_zone = 5
    }   else if (85000 <= end_zip && end_zip <= 99999) {
        var end_zone = 6
    }   else {
        var end_zone = "Unmailable"
    }
    // Calculates total zones package travels through
    total_zones = Math.abs(start_zone - end_zone)
    return total_zones
}

// Function takes in package and total zones and calculates and returns total cost
function cost(package, total_zones) {
    if (package == "Regular Post Card") {
        var cost = .2 + .03*total_zones
    }   else if (package == "Large Post Card") {
        var cost = .37 + .03*total_zones
    }   else if (package == "Envelope") {
        var cost = .37 + .04*total_zones
    }   else if (package == "Large Envelope") {
        var cost = .6 + .05*total_zones
    }   else if (package == "Package") {
        var cost = 2.95 + .25*total_zones
    }   else if (package == "Large Package") {
        var cost = 3.95 + .35*total_zones
    }   else if (package == "Unmailable") {
        var cost = "Unmailable"
    }
    // Code below rounds cost to two decimal points and removes leading '0' if cost is less than 1
    if (typeof cost == "number") {
        cost = cost.toFixed(2)  // Rounds to two decimal points
        if (cost < 1) {
            cost = cost.toString() 
            cost = cost.slice(1)  // Removes leading '0' if cost is less than 1
        }   else {}
    } else {}
    return cost
}

// Main function that calls upon other functions and executes program
function main() {
    values = take_input()
    length = values[0]
    height = values[1]
    thickness = values[2]
    start_zip = values[3]
    end_zip = values[4]
    package = classify_package(length, height, thickness)
    total_zones = classify_zone(start_zip, end_zip)
    if (typeof total_zones == "number") {   
        cost = cost(package, total_zones)
    } else {          
        cost = "Unmailable"
    }
    // Prints the cost by connecting to the element in index.html with the id "print"
    document.getElementById("print").innerHTML = cost
}