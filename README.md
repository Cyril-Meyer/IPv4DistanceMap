# IPv4DistanceMap

The idea is simple: send a ping to each existing ipv4 address to know the time distance.
We can then analyze the results to create a distance map of the internet.

Disclaimer : this is a weekend idea project, not a serious research project.

The result is stored in a (256, 256, 256, 256) shaped numpy array of uint8.
The value in the array correspond to an ip, and the value correspond to the following table.

| value range | signification                                  |
|-------------|------------------------------------------------|
| [0]         | not responding                                 |
| [1, 250]    | ping reponse time in decisecond (10^-1 second) |
| [251, 253]  | unused                                         |
| [254]       | exception                                      |
| [255]       | not pinged yet                                 |

