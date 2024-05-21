# Adapter-pattern

The Adapter Pattern is a design pattern used in programming to allow two incompatible interfaces to work together. It acts like a bridge between two different systems or components, enabling them to communicate with each other without modifying their existing code.

Simple Analogy
Imagine you have an electrical appliance from the United States, which has a plug designed for US power outlets. Now, you travel to Europe, where the power outlets are different, and your plug doesn’t fit. Instead of buying a new appliance, you use a power adapter that lets you plug your US appliance into a European outlet.

In this analogy:

US Plug: The interface of your appliance.

European Outlet: The interface of the European power supply.

Power Adapter: The adapter that makes the US plug compatible with the European outlet.

How It Works in Programming:

In programming, the Adapter Pattern involves three main components:

Client: The system that wants to use an incompatible interface.

Adaptee: The existing interface that needs to be adapted.

Adapter: The bridge that makes the Adaptee’s interface compatible with the Client’s interface.

