import json
import sys

TERMINATORS = 'jmp', 'br', 'ret'

def form_blocks(body):
    cur_block = []
    
    for instr in body:
        if 'op' in instr: # An actual instruction.
            cur_block.append(instr)

            if instr['op'] in TERMINATORS:
                yield cur_block
                cur_block = []
        
        else: # A label.
            yield cur_block
            cur_block = [instr]

    yield cur_block()

def get_cfg(name2block):
    out = {}
    for name, block in name2block.items():
        last = block[-1]
        



def mycfg():
    prog = json.load(sys.stdin)
    for func in prog['functions']:
        name2block = block_map(form_blocks(func['instrs']))
        cfg = get_cfg(name2block)
        print(cfg)
       

def block_map(blocks):
    out = {}

    for block in blocks:
        if 'label' in block[0]:
            name = block[0]['label']
            block = block[1:]
        else:
            name = 'b{}'.format(len(out))

        out[name] = block

        
    return out

            

if __name__ == '__main__':
    mycfg()