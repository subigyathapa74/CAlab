
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity BCD_TO_XS3 is
    Port (
        BCD : in  STD_LOGIC_VECTOR(3 downto 0);  -- BCD input (0-9)
        XS3 : out STD_LOGIC_VECTOR(3 downto 0)   -- Excess-3 output
    );
end entity BCD_TO_XS3;

architecture Behavioral of BCD_TO_XS3 is
begin
    process(BCD)
    begin
        -- Add 3 to the BCD input
        XS3 <= STD_LOGIC_VECTOR(unsigned(BCD) + 3);
    end process;
end architecture Behavioral;
