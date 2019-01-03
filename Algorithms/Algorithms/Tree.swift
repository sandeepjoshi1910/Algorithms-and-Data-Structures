//
//  Tree.swift
//  Algorithms
//
//  Created by Sandeep Joshi on 6/18/18.
//  Copyright © 2018 Sandeep Joshi. All rights reserved.
//

import Cocoa

class TNode: NSObject {
    var data: Int?
    var left: TNode?
    var right: TNode?

    init(data: Int) {
        self.data = data
        self.left = nil
        self.right = nil
    }
}

class Tree: NSObject {
    
    var treeRoot: TNode? = nil
    
    func insertNode(value: Int, node: TNode?) {
        
        if self.treeRoot == nil {
            self.treeRoot = TNode(data: value)
            return
        }
        
        if value > node!.data! {
            if node!.right != nil {
                self.insertNode(value: value, node: node!.right)
            } else {
                let new_node = TNode(data: value)
                node!.right = new_node
                return
            }
        } else {
            if node!.left != nil {
                self.insertNode(value: value, node: node!.left)
            } else {
                let new_node = TNode(data: value)
                node!.left = new_node
                return
            }
        }
        
        
    }

    func inorder(node: TNode?) {
        if node == nil {
            return
        }

        inorder(node: node!.left)
        print(node!.data!)
        inorder(node: node!.right)
        
    }

    func preorder(node: TNode?) {
        if node == nil {
            return
        }

        print(node!.data!)
        preorder(node: node!.left)
        preorder(node: node!.right)
    }

    func postorder(node: TNode?) {

        if node == nil {
            return
        }

        postorder(node: node!.left)
        postorder(node: node!.right)
        print(node!.data!)
    }
    
    
    
}
//
//
//var t = Tree()
//let nums = [25,15,10,4,12,22,18,24,50,35,31,44,70,66,90]
//
//for num in nums {
//    t.insertNode(value: num, node: t.treeRoot)
//}
//
//t.postorder(node: t.treeRoot)
