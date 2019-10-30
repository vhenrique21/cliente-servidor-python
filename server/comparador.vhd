-- comparador.vhd
--     comparador binario com entradas de 2 bits

library IEEE;
use IEEE.std_logic_1164.all;

entity comparador is
    port (
        A, B                : in std_logic_vector (3 downto 0);
        igual, menor, maior : out STD_LOGIC
    );
end comparador;

architecture comportamental of comparador is
begin

    igual <= '1' when A=B else '0';
    menor <= '1' when A<B else '0';
    maior <= '1' when A>B else '0';

end comportamental;
