# AXI4-Lite Register Bank (`axil_regbank`)

## 1. Module Parameters
- `ADDR_WIDTH = 4`
- `DATA_WIDTH = 32`

## 2. Clock & Reset
- `ACLK` : Clock input
- `ARESETn` : Active-low reset

## 3. AXI Write Channels
### 3.1 Write Address Channel (AW)
- `saxi_awaddr` : Address
- `saxi_awvalid` : Master asserts when address valid
- `saxi_awready` : Slave ready to accept address
- Latching mechanism:
  - `aw_hs_done` : handshake done
  - `awaddr_q` : latched address

### 3.2 Write Data Channel (W)
- `saxi_wdata` : Data bus
- `saxi_wstrb` : Byte-enable strobes
- `saxi_wvalid` : Data valid
- `saxi_wready` : Slave ready
- Latching mechanism:
  - `w_hs_done` : handshake done
  - `wdata_q` : latched data
  - `wstrb_q` : latched strobe

### 3.3 Write Response Channel (B)
- `saxi_bresp` : 2-bit response (OKAY / SLVERR)
- `saxi_bvalid` : Response valid
- `saxi_bready` : Master ready to accept
- Behavior:
  - Set after both AW & W latched (`do_write`)
  - Address decoding:
    - `0x0` → CTRL register
    - `0x4` → DATA register
    - Others → SLVERR
  - WSTRB applied per byte

## 4. AXI Read Channels
### 4.1 Read Address Channel (AR)
- `saxi_araddr` : Address
- `saxi_arvalid` : Master asserts
- `saxi_arready` : Slave ready
- Latching mechanism:
  - `ar_hs_done` : handshake done
  - `araddr_q` : latched address

### 4.2 Read Data Channel (R)
- `saxi_rdata` : Read data (32 bits)
- `saxi_rresp` : 2-bit response (OKAY / SLVERR)
- `saxi_rvalid` : Valid signal
- `saxi_rready` : Master ready
- Behavior:
  - On AR handshake, prepare `rdata` + `rresp`
  - Address decoding:
    - `0x0` → CTRL
    - `0x4` → DATA
    - Others → SLVERR
  - Transfer occurs when `RVALID && RREADY`

## 5. Internal Registers
- `reg_ctrl` : Control register @ 0x0
- `reg_data` : Data register @ 0x4

## 6. Handshake Logic
- Write:
  - Capture AW & W independently
  - Perform write when both captured (`do_write`)
  - Clear handshake after B accepted
- Read:
  - Capture AR
  - Prepare RDATA + RRESP immediately
  - Clear handshake after R accepted

## 7. Address Decoding
- Using word offset (`addr[3:2]`) for 32-bit words:
  - `2'b00` → CTRL
  - `2'b01` → DATA
  - Others → SLVERR

## 8. Key AXI4-Lite Concepts Illustrated
- Write: 3 channels (AW, W, B)
- Read: 2 channels (AR, R)
- `RDATA + RRESP` transferred together (34-bit logical payload)
- WSTRB: byte-wise write enable
- OKAY / SLVERR responses
- Independent arrival of address & data for write