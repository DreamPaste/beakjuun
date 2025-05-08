import readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input: string[] = [];
rl.on('line', line => {
  input.push(line.trim());
}).on('close', () => {
  solve();
  process.exit();
});
type Tree = {
  [key: string]: [string, string]; // node: [left, right]
};

function solve() {
  const preorder: string[] = [];
  const inorder: string[] = [];
  const postorder: string[] = [];

  const tree: Tree = (() => {
    const tree: Tree = {};
    const N = Number(input[0]);
    for (let i = 1; i <= N; i++) {
      const [node, leftCh, rightCh] = input[i].split(' ');
      tree[node] = [leftCh, rightCh];
    }
    return tree;
  })();

  function preOrder(node: string) {
    if (node === '.') return;
    const [left, right] = tree[node];
    preorder.push(node);
    preOrder(left);
    preOrder(right);
  }

  function inOrder(node: string) {
    if (node === '.') return;
    const [left, right] = tree[node];
    inOrder(left);
    inorder.push(node);
    inOrder(right);
  }

  function postOrder(node: string) {
    if (node === '.') return;
    const [left, right] = tree[node];
    postOrder(left);
    postOrder(right);
    postorder.push(node);
  }
  preOrder('A');
  inOrder('A');
  postOrder('A');

  console.log(preorder.join(''));
  console.log(inorder.join(''));
  console.log(postorder.join(''));
}
