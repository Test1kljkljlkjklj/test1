<?php

declare(strict_types=1);

namespace App\Order;

final class Threshold
{
    public static function accepts(int $orderTotalEur, \DateTimeImmutable $orderedAt): bool
    {
        $firstDayAt150 = new \DateTimeImmutable('2026-12-01 00:00:00', new \DateTimeZone('Europe/Madrid'));
        $minimumEur = $orderedAt >= $firstDayAt150 ? 150 : 100;

        return $orderTotalEur >= $minimumEur;
    }
}
