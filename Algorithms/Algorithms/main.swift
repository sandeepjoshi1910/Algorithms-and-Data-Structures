//
//  main.swift
//  Algorithms
//
//  Created by Sandeep Joshi on 6/17/18.
//  Copyright © 2018 Sandeep Joshi. All rights reserved.
//

import Foundation


let str = "Sandeep"
let str1 = "hfgawwt"

for i in 0..<str.count {
    let index = str.index(str.startIndex, offsetBy: i)
    let diff = abs(Int(str1[index].unicodeScalars.first?.value as! UInt32) - Int(str[index].unicodeScalars.first?.value as! UInt32))
    print(diff)
}
