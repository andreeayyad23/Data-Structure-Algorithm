class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  class Queue {
    constructor() {
      this.head = null;
      this.tail = null;
    }
  
    enqueue(value) {
      const newNode = new Node(value);
      if (this.tail === null) {
        this.head = this.tail = newNode;
      } else {
        this.tail.next = newNode;
        this.tail = newNode;
      }
    }
  
    dequeue() {
      if (this.head === null) {
        return null;
      }
      
      const temp = this.head;
      this.head = this.head.next;
  
      if (this.head === null) {
        this.tail = null;
      }
  
      return temp.value;
    }
  
    isEmpty() {
      return this.head === null;
    }
  
    peek() {
      if (this.head === null) {
        return null;
      }
      return this.head.value;
    }
  }
  
  const queue = new Queue();
  queue.enqueue(5);
  queue.enqueue(8);
  queue.enqueue(9);
  
  console.log(queue.dequeue());
  console.log(queue.dequeue());
  console.log(queue.peek());
  console.log(queue.isEmpty());
  console.log(queue.dequeue());
  console.log(queue.isEmpty());
  